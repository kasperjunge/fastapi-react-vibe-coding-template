import { api } from '@/shared/services/api';
import { User } from '@/shared/types';

export interface LoginCredentials {
  email: string;
  password: string;
}

export interface AuthResponse {
  user: User;
  token: string;
}

export const authService = {
  /**
   * Login user and retrieve authentication token
   */
  login: async (credentials: LoginCredentials): Promise<AuthResponse> => {
    const data = await api.post<AuthResponse>('/auth/login', credentials);
    // Store token in localStorage for future requests
    if (data.token) {
      localStorage.setItem('auth_token', data.token);
    }
    return data;
  },

  /**
   * Register a new user account
   */
  register: async (userData: LoginCredentials & { name: string }): Promise<AuthResponse> => {
    const data = await api.post<AuthResponse>('/auth/register', userData);
    // Store token in localStorage for future requests
    if (data.token) {
      localStorage.setItem('auth_token', data.token);
    }
    return data;
  },

  /**
   * Logout user (clear token and session)
   */
  logout: async (): Promise<void> => {
    try {
      await api.post('/auth/logout', {});
    } catch (error) {
      console.error('Logout error:', error);
    } finally {
      localStorage.removeItem('auth_token');
    }
  },

  /**
   * Get current user profile
   */
  getCurrentUser: async (): Promise<User> => {
    const data = await api.get<User>('/auth/me');
    return data;
  },

  /**
   * Check if user is authenticated
   */
  isAuthenticated: (): boolean => {
    return !!localStorage.getItem('auth_token');
  },
}; 