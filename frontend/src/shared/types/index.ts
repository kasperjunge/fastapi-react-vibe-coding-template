/**
 * Common types used across the application
 */

export type User = {
  id: string;
  email: string;
  name: string;
  role: 'user' | 'admin';
  createdAt: string;
  updatedAt: string;
};

export type ApiResponse<T> = {
  data: T;
  message?: string;
  errors?: Record<string, string[]>;
};

export type PaginatedResponse<T> = {
  data: T[];
  meta: {
    currentPage: number;
    totalPages: number;
    totalItems: number;
    itemsPerPage: number;
  };
};

export type SortDirection = 'asc' | 'desc';

export type QueryParams = {
  page?: number;
  limit?: number;
  sort?: string;
  order?: SortDirection;
  search?: string;
  filters?: Record<string, string | number | boolean>;
}; 