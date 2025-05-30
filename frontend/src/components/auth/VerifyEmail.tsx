import { useState, useEffect } from 'react'
import { useParams, useNavigate } from 'react-router-dom'
import { useAuth } from '../../App'

const VerifyEmail = () => {
  const { token } = useParams<{ token: string }>()
  const navigate = useNavigate()
  const { setUser } = useAuth()
  const [status, setStatus] = useState<'verifying' | 'success' | 'error'>('verifying')
  const [errorMessage, setErrorMessage] = useState('')

  useEffect(() => {
    const verifyEmail = async () => {
      if (!token) {
        setStatus('error')
        setErrorMessage('Invalid verification link')
        return
      }

      try {
        const response = await fetch('/api/auth/verify', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({ token }),
        })

        if (response.ok) {
          const userData = await response.json()
          setUser(userData)
          setStatus('success')
          
          // Redirect to success page after a short delay
          setTimeout(() => {
            navigate('/success', { 
              state: { 
                message: 'Email verified successfully!',
                type: 'verification'
              } 
            })
          }, 2000)
        } else {
          const errorData = await response.json()
          setStatus('error')
          
          switch (errorData.detail) {
            case 'VERIFY_USER_BAD_TOKEN':
              setErrorMessage('Invalid or expired verification link. Please request a new verification email.')
              break
            case 'VERIFY_USER_ALREADY_VERIFIED':
              setErrorMessage('Your email is already verified. You can now log in to your account.')
              break
            default:
              setErrorMessage(errorData.detail || 'Verification failed')
          }
        }
      } catch {
        setStatus('error')
        setErrorMessage('Network error. Please check your connection and try again.')
      }
    }

    verifyEmail()
  }, [token, navigate, setUser])

  if (status === 'verifying') {
    return (
      <div className="min-h-screen flex items-center justify-center px-4">
        <div className="max-w-md w-full space-y-8 text-center">
          <div className="mx-auto h-16 w-16 text-blue-600">
            <svg className="animate-spin" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4"></circle>
              <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
            </svg>
          </div>
          <h2 className="text-3xl font-extrabold text-gray-900">
            Verifying Your Email
          </h2>
          <p className="text-sm text-gray-600">
            Please wait while we verify your email address...
          </p>
        </div>
      </div>
    )
  }

  if (status === 'success') {
    return (
      <div className="min-h-screen flex items-center justify-center px-4">
        <div className="max-w-md w-full space-y-8 text-center">
          <div className="mx-auto h-16 w-16 text-green-600">
            <svg fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
            </svg>
          </div>
          <h2 className="text-3xl font-extrabold text-gray-900">
            Email Verified!
          </h2>
          <p className="text-sm text-gray-600">
            Your email has been successfully verified. Redirecting you now...
          </p>
        </div>
      </div>
    )
  }

  // Error state
  return (
    <div className="min-h-screen flex items-center justify-center px-4">
      <div className="max-w-md w-full space-y-8">
        <div className="text-center">
          <div className="mx-auto h-16 w-16 text-red-600">
            <svg fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-2.5L13.732 4c-.77-.833-1.964-.833-2.732 0L4.082 16.5c-.77.833.192 2.5 1.732 2.5z" />
            </svg>
          </div>
          <h2 className="mt-6 text-3xl font-extrabold text-gray-900">
            Verification Failed
          </h2>
          <p className="mt-2 text-sm text-gray-600">
            {errorMessage}
          </p>
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
                What can you do?
              </h3>
              <div className="mt-2 text-sm text-red-700">
                <ul className="list-disc list-inside space-y-1">
                  <li>Request a new verification email</li>
                  <li>Check if you're using the latest verification link</li>
                  <li>Contact support if the problem persists</li>
                </ul>
              </div>
            </div>
          </div>
        </div>

        <div className="flex space-x-4">
          <button
            onClick={() => navigate('/verification-status')}
            className="flex-1 flex justify-center py-2 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-blue-600 hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500"
          >
            Request New Email
          </button>
          <button
            onClick={() => navigate('/register')}
            className="flex-1 flex justify-center py-2 px-4 border border-gray-300 text-sm font-medium rounded-md text-gray-700 bg-white hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500"
          >
            Back to Registration
          </button>
        </div>
      </div>
    </div>
  )
}

export default VerifyEmail 