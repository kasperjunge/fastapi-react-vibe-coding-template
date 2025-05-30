import { useState, useEffect } from 'react'
import { useLocation, useNavigate } from 'react-router-dom'
import { Button } from '../ui/button'

interface LocationState {
  email?: string
}

const VerificationStatus = () => {
  const location = useLocation()
  const navigate = useNavigate()
  const state = location.state as LocationState
  const [email, setEmail] = useState(state?.email || '')
  const [isResending, setIsResending] = useState(false)
  const [resendMessage, setResendMessage] = useState('')
  const [resendCooldown, setResendCooldown] = useState(0)

  // Cooldown timer
  useEffect(() => {
    if (resendCooldown > 0) {
      const timer = setTimeout(() => {
        setResendCooldown(resendCooldown - 1)
      }, 1000)
      return () => clearTimeout(timer)
    }
  }, [resendCooldown])

  const handleResendVerification = async () => {
    if (!email) {
      setResendMessage('Please enter your email address')
      return
    }

    setIsResending(true)
    setResendMessage('')

    try {
      const response = await fetch('/api/auth/request-verify-token', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ email }),
      })

      if (response.ok) {
        setResendMessage('Verification email sent! Please check your inbox.')
        setResendCooldown(60) // 60 second cooldown
      } else {
        const errorData = await response.json()
        setResendMessage(errorData.detail || 'Failed to send verification email')
      }
    } catch {
      setResendMessage('Network error. Please try again.')
    } finally {
      setIsResending(false)
    }
  }

  const handleEmailChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setEmail(e.target.value)
    if (resendMessage) setResendMessage('')
  }

  return (
    <div className="min-h-screen flex items-center justify-center px-4">
      <div className="max-w-md w-full space-y-8">
        <div className="text-center">
          <div className="mx-auto h-16 w-16 text-blue-600">
            <svg fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M3 8l7.89 4.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z" />
            </svg>
          </div>
          <h2 className="mt-6 text-3xl font-extrabold text-gray-900">
            Check Your Email
          </h2>
          <p className="mt-2 text-sm text-gray-600">
            We've sent a verification link to your email address
          </p>
        </div>

        <div className="bg-yellow-50 border border-yellow-200 rounded-md p-4">
          <div className="flex">
            <div className="flex-shrink-0">
              <svg className="h-5 w-5 text-yellow-400" fill="currentColor" viewBox="0 0 20 20">
                <path fillRule="evenodd" d="M8.257 3.099c.765-1.36 2.722-1.36 3.486 0l5.58 9.92c.75 1.334-.213 2.98-1.742 2.98H4.42c-1.53 0-2.493-1.646-1.743-2.98l5.58-9.92zM11 13a1 1 0 11-2 0 1 1 0 012 0zm-1-8a1 1 0 00-1 1v3a1 1 0 002 0V6a1 1 0 00-1-1z" clipRule="evenodd" />
              </svg>
            </div>
            <div className="ml-3">
              <h3 className="text-sm font-medium text-yellow-800">
                Verification Required
              </h3>
              <div className="mt-2 text-sm text-yellow-700">
                <p>
                  You must verify your email address before you can access your account. 
                  Please check your inbox and spam folder for the verification email.
                </p>
              </div>
            </div>
          </div>
        </div>

        <div className="space-y-4">
          <div>
            <label htmlFor="email" className="block text-sm font-medium text-gray-700">
              Email address
            </label>
            <input
              id="email"
              name="email"
              type="email"
              value={email}
              onChange={handleEmailChange}
              className="mt-1 appearance-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-md focus:outline-none focus:ring-blue-500 focus:border-blue-500 focus:z-10 sm:text-sm"
              placeholder="Enter your email to resend verification"
            />
          </div>

          {resendMessage && (
            <div className={`border rounded-md p-4 ${
              resendMessage.includes('sent') || resendMessage.includes('Verification email sent')
                ? 'bg-green-50 border-green-200'
                : 'bg-red-50 border-red-200'
            }`}>
              <div className="flex">
                <div className="flex-shrink-0">
                  {resendMessage.includes('sent') || resendMessage.includes('Verification email sent') ? (
                    <svg className="h-5 w-5 text-green-400" fill="currentColor" viewBox="0 0 20 20">
                      <path fillRule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clipRule="evenodd" />
                    </svg>
                  ) : (
                    <svg className="h-5 w-5 text-red-400" fill="currentColor" viewBox="0 0 20 20">
                      <path fillRule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zM8.707 7.293a1 1 0 00-1.414 1.414L8.586 10l-1.293 1.293a1 1 0 101.414 1.414L10 11.414l1.293 1.293a1 1 0 001.414-1.414L11.414 10l1.293-1.293a1 1 0 00-1.414-1.414L10 8.586 8.707 7.293z" clipRule="evenodd" />
                    </svg>
                  )}
                </div>
                <div className="ml-3">
                  <p className={`text-sm ${
                    resendMessage.includes('sent') || resendMessage.includes('Verification email sent')
                      ? 'text-green-800'
                      : 'text-red-800'
                  }`}>
                    {resendMessage}
                  </p>
                </div>
              </div>
            </div>
          )}

          <Button
            onClick={handleResendVerification}
            disabled={isResending || resendCooldown > 0 || !email}
            className="w-full flex justify-center py-2 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-blue-600 hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500 disabled:opacity-50 disabled:cursor-not-allowed"
          >
            {isResending ? (
              <>
                <svg className="animate-spin -ml-1 mr-3 h-5 w-5 text-white" fill="none" viewBox="0 0 24 24">
                  <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4"></circle>
                  <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
                </svg>
                Sending...
              </>
            ) : resendCooldown > 0 ? (
              `Resend in ${resendCooldown}s`
            ) : (
              'Resend verification email'
            )}
          </Button>

          <div className="text-center">
            <button
              onClick={() => navigate('/register')}
              className="text-sm text-blue-600 hover:text-blue-500"
            >
              ← Back to registration
            </button>
          </div>
        </div>

        <div className="bg-gray-50 border border-gray-200 rounded-md p-4">
          <h3 className="text-sm font-medium text-gray-800 mb-2">
            Didn't receive the email?
          </h3>
          <ul className="text-sm text-gray-600 space-y-1">
            <li>• Check your spam/junk folder</li>
            <li>• Make sure you entered the correct email address</li>
            <li>• Wait a few minutes for the email to arrive</li>
            <li>• Try resending the verification email</li>
          </ul>
        </div>
      </div>
    </div>
  )
}

export default VerificationStatus 