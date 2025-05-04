/**
 * Base API service for making HTTP requests
 */

const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000/api';

type RequestOptions = {
  method?: 'GET' | 'POST' | 'PUT' | 'DELETE' | 'PATCH';
  headers?: Record<string, string>;
  body?: any;
  withCredentials?: boolean;
};

export async function fetchApi<T>(
  endpoint: string,
  options: RequestOptions = {}
): Promise<T> {
  const {
    method = 'GET',
    headers = {},
    body,
    withCredentials = true,
  } = options;

  const requestHeaders: HeadersInit = {
    'Content-Type': 'application/json',
    ...headers,
  };

  // Get token from local storage if it exists
  const token = localStorage.getItem('auth_token');
  if (token) {
    requestHeaders.Authorization = `Bearer ${token}`;
  }

  const config: RequestInit = {
    method,
    headers: requestHeaders,
    credentials: withCredentials ? 'include' : 'same-origin',
    body: body ? JSON.stringify(body) : undefined,
  };

  const response = await fetch(`${API_URL}${endpoint}`, config);

  // Handle non-JSON responses
  const contentType = response.headers.get('content-type');
  if (contentType && contentType.includes('application/json')) {
    const data = await response.json();
    
    // Handle API error responses
    if (!response.ok) {
      throw new ApiError(response.status, data.message || 'An error occurred', data);
    }
    
    return data;
  } else {
    if (!response.ok) {
      throw new ApiError(
        response.status,
        'An error occurred',
        await response.text()
      );
    }
    
    return await response.text() as unknown as T;
  }
}

export class ApiError extends Error {
  status: number;
  data: any;

  constructor(status: number, message: string, data?: any) {
    super(message);
    this.name = 'ApiError';
    this.status = status;
    this.data = data;
  }
}

// Shorthand methods for common HTTP verbs
export const api = {
  get: <T>(endpoint: string, options?: Omit<RequestOptions, 'method' | 'body'>) =>
    fetchApi<T>(endpoint, { ...options, method: 'GET' }),
    
  post: <T>(endpoint: string, body: any, options?: Omit<RequestOptions, 'method'>) =>
    fetchApi<T>(endpoint, { ...options, method: 'POST', body }),
    
  put: <T>(endpoint: string, body: any, options?: Omit<RequestOptions, 'method'>) =>
    fetchApi<T>(endpoint, { ...options, method: 'PUT', body }),
    
  patch: <T>(endpoint: string, body: any, options?: Omit<RequestOptions, 'method'>) =>
    fetchApi<T>(endpoint, { ...options, method: 'PATCH', body }),
    
  delete: <T>(endpoint: string, options?: Omit<RequestOptions, 'method'>) =>
    fetchApi<T>(endpoint, { ...options, method: 'DELETE' }),
}; 