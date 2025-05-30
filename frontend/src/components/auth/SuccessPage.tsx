import { useLocation, useNavigate } from 'react-router-dom'
import { useAuth } from '../../App'
import { Button } from '../ui/button'

interface LocationState {
  message?: string
  type?: 'verification' | 'registration' | 'general'
}

const SuccessPage = () => {
  const location = useLocation()
  const navigate = useNavigate()
  const { user } = useAuth()
  const state = location.state as LocationState

  const message = state?.message || 'Operation completed successfully!'
  const type = state?.type || 'general'

  const handleContinue = () => {
    if (user && user.is_verified) {
      navigate('/dashboard')
    } else {
      navigate('/register')
    }
  }

  const getIcon = () => {
    switch (type) {
      case 'verification':
        return (
          <svg fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M3 8l7.89 4.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z" />
          </svg>
        )
      case 'registration':
        return (
          <svg fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M18 9v3m0 0v3m0-3h3m-3 0h-3m-2-5a4 4 0 11-8 0 4 4 0 018 0zM3 20a6 6 0 0112 0v1H3v-1z" />
          </svg>
        )
      default:
        return (
          <svg fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
          </svg>
        )
    }
  }

  const getTitle = () => {
    switch (type) {
      case 'verification':
        return 'Email Verified!'
      case 'registration':
        return 'Registration Complete!'
      default:
        return 'Success!'
    }
  }

  const getSubtitle = () => {
    switch (type) {
      case 'verification':
        return 'Your email has been successfully verified. You can now access your account.'
      case 'registration':
        return 'Your account has been created successfully.'
      default:
        return 'Your request has been processed successfully.'
    }
  }

  return (
    <div className="min-h-screen flex items-center justify-center px-4">
      <div className="max-w-md w-full space-y-8">
        <div className="text-center">
          <div className="mx-auto h-16 w-16 text-green-600">
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
        </div>

        <div className="bg-green-50 border border-green-200 rounded-md p-4">
          <div className="flex">
            <div className="flex-shrink-0">
              <svg className="h-5 w-5 text-green-400" fill="currentColor" viewBox="0 0 20 20">
                <path fillRule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clipRule="evenodd" />
              </svg>
            </div>
            <div className="ml-3">
              <h3 className="text-sm font-medium text-green-800">
                What's next?
              </h3>
              <div className="mt-2 text-sm text-green-700">
                {type === 'verification' && user?.is_verified ? (
                  <p>You can now access your dashboard and start using the application.</p>
                ) : type === 'verification' ? (
                  <p>You can now log in to your account and start using the application.</p>
                ) : (
                  <p>You can continue with your next steps.</p>
                )}
              </div>
            </div>
          </div>
        </div>

        <div className="space-y-3">
          <Button
            onClick={handleContinue}
            className="w-full flex justify-center py-2 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-green-600 hover:bg-green-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-green-500"
          >
            {user && user.is_verified ? 'Go to Dashboard' : 'Continue'}
          </Button>

          {type === 'verification' && (
            <div className="text-center">
              <p className="text-sm text-gray-600">
                Welcome to the platform! 🎉
              </p>
            </div>
          )}
        </div>

        {/* Additional helpful information */}
        <div className="bg-gray-50 border border-gray-200 rounded-md p-4">
          <h3 className="text-sm font-medium text-gray-800 mb-2">
            Need help?
          </h3>
          <ul className="text-sm text-gray-600 space-y-1">
            <li>• Check out our getting started guide</li>
            <li>• Browse the help documentation</li>
            <li>• Contact support if you have questions</li>
          </ul>
        </div>
      </div>
    </div>
  )
}

export default SuccessPage 