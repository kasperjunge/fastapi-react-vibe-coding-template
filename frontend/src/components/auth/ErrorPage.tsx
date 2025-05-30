import { useLocation, useNavigate } from 'react-router-dom'
import { Button } from '../ui/button'

interface LocationState {
  message?: string
  type?: 'verification' | 'registration' | 'network' | 'general'
  details?: string
}

const ErrorPage = () => {
  const location = useLocation()
  const navigate = useNavigate()
  const state = location.state as LocationState

  const message = state?.message || 'Something went wrong'
  const type = state?.type || 'general'
  const details = state?.details

  const getIcon = () => {
    switch (type) {
      case 'verification':
        return (
          <svg fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M3 8l7.89 4.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z" />
          </svg>
        )
      case 'network':
        return (
          <svg fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M8.111 16.404a5.5 5.5 0 017.778 0M12 20h.01m-7.08-7.071c3.904-3.905 10.236-3.905 14.141 0M1.394 9.393c5.857-5.857 15.355-5.857 21.213 0" />
          </svg>
        )
      default:
        return (
          <svg fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-2.5L13.732 4c-.77-.833-1.964-.833-2.732 0L4.082 16.5c-.77.833.192 2.5 1.732 2.5z" />
          </svg>
        )
    }
  }

  const getTitle = () => {
    switch (type) {
      case 'verification':
        return 'Verification Failed'
      case 'registration':
        return 'Registration Failed'
      case 'network':
        return 'Connection Error'
      default:
        return 'Error Occurred'
    }
  }

  const getSubtitle = () => {
    switch (type) {
      case 'verification':
        return 'We couldn\'t verify your email address.'
      case 'registration':
        return 'We couldn\'t create your account.'
      case 'network':
        return 'Please check your internet connection and try again.'
      default:
        return 'An unexpected error has occurred.'
    }
  }

  const getRecoveryOptions = () => {
    switch (type) {
      case 'verification':
        return [
          {
            label: 'Request New Verification Email',
            action: () => navigate('/verification-status'),
            primary: true
          },
          {
            label: 'Back to Registration',
            action: () => navigate('/register'),
            primary: false
          }
        ]
      case 'registration':
        return [
          {
            label: 'Try Again',
            action: () => navigate('/register'),
            primary: true
          }
        ]
      case 'network':
        return [
          {
            label: 'Retry',
            action: () => window.location.reload(),
            primary: true
          },
          {
            label: 'Go Back',
            action: () => navigate(-1),
            primary: false
          }
        ]
      default:
        return [
          {
            label: 'Go Home',
            action: () => navigate('/'),
            primary: true
          }
        ]
    }
  }

  const getTroubleshootingTips = () => {
    switch (type) {
      case 'verification':
        return [
          'Check if you\'re using the latest verification link',
          'Make sure the link hasn\'t expired',
          'Try requesting a new verification email',
          'Check your spam/junk folder for the email'
        ]
      case 'registration':
        return [
          'Make sure all required fields are filled correctly',
          'Check if your email address is valid',
          'Ensure your password meets the requirements',
          'Try using a different email address'
        ]
      case 'network':
        return [
          'Check your internet connection',
          'Try refreshing the page',
          'Disable any VPN or proxy',
          'Try again in a few minutes'
        ]
      default:
        return [
          'Try refreshing the page',
          'Clear your browser cache',
          'Try using a different browser',
          'Contact support if the problem persists'
        ]
    }
  }

  return (
    <div className="min-h-screen flex items-center justify-center px-4">
      <div className="max-w-md w-full space-y-8">
        <div className="text-center">
          <div className="mx-auto h-16 w-16 text-red-600">
            {getIcon()}
          </div>
          <h2 className="mt-6 text-3xl font-extrabold text-gray-900">
            {getTitle()}
          </h2>
          <p className="mt-2 text-sm text-gray-600">
            {getSubtitle()}
          </p>
          {message !== getSubtitle() && (
            <p className="mt-2 text-sm text-gray-800 font-medium">
              {message}
            </p>
          )}
          {details && (
            <p className="mt-2 text-xs text-gray-500 font-mono bg-gray-100 p-2 rounded">
              {details}
            </p>
          )}
        </div>

        <div className="bg-red-50 border border-red-200 rounded-md p-4">
          <div className="flex">
            <div className="flex-shrink-0">
              <svg className="h-5 w-5 text-red-400" fill="currentColor" viewBox="0 0 20 20">
                <path fillRule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zM8.707 7.293a1 1 0 00-1.414 1.414L8.586 10l-1.293 1.293a1 1 0 101.414 1.414L10 11.414l1.293 1.293a1 1 0 001.414-1.414L11.414 10l1.293-1.293a1 1 0 00-1.414-1.414L10 8.586 8.707 7.293z" clipRule="evenodd" />
              </svg>
            </div>
            <div className="ml-3">
              <h3 className="text-sm font-medium text-red-800">
                What can you try?
              </h3>
              <div className="mt-2 text-sm text-red-700">
                <ul className="list-disc list-inside space-y-1">
                  {getTroubleshootingTips().map((tip, index) => (
                    <li key={index}>{tip}</li>
                  ))}
                </ul>
              </div>
            </div>
          </div>
        </div>

        <div className="space-y-3">
          {getRecoveryOptions().map((option, index) => (
            <Button
              key={index}
              onClick={option.action}
              className={`w-full flex justify-center py-2 px-4 border text-sm font-medium rounded-md focus:outline-none focus:ring-2 focus:ring-offset-2 ${
                option.primary
                  ? 'border-transparent text-white bg-red-600 hover:bg-red-700 focus:ring-red-500'
                  : 'border-gray-300 text-gray-700 bg-white hover:bg-gray-50 focus:ring-blue-500'
              }`}
            >
              {option.label}
            </Button>
          ))}
        </div>

        {/* Additional help section */}
        <div className="bg-gray-50 border border-gray-200 rounded-md p-4">
          <h3 className="text-sm font-medium text-gray-800 mb-2">
            Still need help?
          </h3>
          <div className="text-sm text-gray-600 space-y-2">
            <p>If you continue to experience issues, please:</p>
            <ul className="list-disc list-inside space-y-1 ml-2">
              <li>Contact our support team</li>
              <li>Check our status page for known issues</li>
              <li>Visit our help documentation</li>
            </ul>
          </div>
        </div>
      </div>
    </div>
  )
}

export default ErrorPage 