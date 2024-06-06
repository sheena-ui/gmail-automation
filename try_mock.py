import pytest
from try_refactor import MFALogin


@pytest.fixture(autouse=True)
def mock_mfa_auth_app(mocker):
    mocker.patch.object(MFALogin, 'auth_app')


def create_mock_wrapper_fn(mocker, status_code=400):
    mock_wrapper_fn = mocker.Mock()
    response = mocker.Mock(status_code=status_code)
    mock_wrapper_fn.return_value = response
    return mock_wrapper_fn

class TestMFALogin:
    def test_mfa_login_auth_app_499(self, mocker):
        mfa_login, create_mock_wrapper_fn, create_mock_response = mock_mfa_login

        # Create a mock for auth_app method
        mock_wrapper_fn = create_mock_wrapper_fn('auth_app')

        # Create a mock response with status code 499
        response_499 = create_mock_response(499)
        mock_wrapper_fn.return_value = response_499

        # Call the __get__ method to obtain the wrapped function
        wrapped_function = mfa_login.__get__(None)

        # Call the wrapped function with any necessary arguments
        wrapped_function()

        # Assert that auth_app was called
        mfa_login.auth_app.assert_called_once()