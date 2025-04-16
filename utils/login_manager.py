import secrets
import streamlit as st
import streamlit_authenticator as stauth
from utils.data_manager import DataManager


class LoginManager:
    def __new__(cls, *args, **kwargs):
        if 'login_manager' in st.session_state:
            return st.session_state.login_manager
        else:
            instance = super(LoginManager, cls).__new__(cls)
            st.session_state.login_manager = instance
            return instance

    def __init__(self, data_manager: DataManager = None,
                 auth_credentials_file: str = 'credentials.yaml',
                 auth_cookie_name: str = 'bmld_inf2_streamlit_app'):
        if hasattr(self, 'authenticator'):
            return

        if data_manager is None:
            return

        self.data_manager = data_manager
        self.auth_credentials_file = auth_credentials_file
        self.auth_cookie_name = auth_cookie_name
        self.auth_cookie_key = secrets.token_urlsafe(32)
        self.auth_credentials = self._load_auth_credentials()
        self.authenticator = stauth.Authenticate(
            self.auth_credentials, self.auth_cookie_name, self.auth_cookie_key
        )

    def _load_auth_credentials(self):
        dh = self.data_manager._get_data_handler()
        return dh.load(self.auth_credentials_file, initial_value={"usernames": {}})

    def _save_auth_credentials(self):
        dh = self.data_manager._get_data_handler()
        dh.save(self.auth_credentials_file, self.auth_credentials)

    def login_register(self, login_title='Login', register_title='Register new user'):
        if st.session_state.get("authentication_status") is True:
            self.authenticator.logout()
        else:
            login_tab, register_tab = st.tabs((login_title, register_title))
            with login_tab:
                st.markdown("""
                    <div style='text-align: center; font-size: 32px; font-weight: bold;'>
                        Herzlich willkommen in deinem Laborjournal 🧪
                    </div>
                """, unsafe_allow_html=True)

                self.login(stop=False)

            with register_tab:
                self.register()

    def login(self, stop=True):
        if st.session_state.get("authentication_status") is True:
            self.authenticator.logout()
        else:
            self.authenticator.login()
            if st.session_state["authentication_status"] is False:
                st.error("Username/password is incorrect")
            if stop:
                st.stop()

    def register(self, stop=True):
        if st.session_state.get("authentication_status") is True:
            self.authenticator.logout()
        else:
            st.info("""
                The password must be 8-20 characters long and include at least one uppercase letter, 
                one lowercase letter, one digit, and one special character from @$!%*?&.
            """)
            res = self.authenticator.register_user()
            if res[1] is not None:
                st.success(f"User {res[1]} registered successfully")
                try:
                    self._save_auth_credentials()
                    st.success("Credentials saved successfully")
                except Exception as e:
                    st.error(f"Failed to save credentials: {e}")
            if stop:
                st.stop()

    def go_to_login(self, login_page_py_file):
        if st.session_state.get("authentication_status") is not True:
            st.switch_page(login_page_py_file)
        else:
            self.authenticator.logout()
