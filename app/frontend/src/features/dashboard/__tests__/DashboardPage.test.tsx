import { describe, it, expect, vi, beforeEach } from 'vitest';
import { render, screen, waitFor } from '@testing-library/react';
import { BrowserRouter } from 'react-router-dom';
import DashboardPage from '../DashboardPage';
import { dashboardService } from '../dashboardService';

// Mock the services and navigation
const mockNavigate = vi.fn();
vi.mock('react-router-dom', () => ({
  ...vi.importActual('react-router-dom'),
  useNavigate: () => mockNavigate,
}));

vi.mock('../dashboardService', () => ({
  dashboardService: {
    getDashboardStats: vi.fn(),
  },
}));

describe('DashboardPage', () => {
  beforeEach(() => {
    vi.clearAllMocks();
    // Reset mock implementations
    vi.mocked(dashboardService.getDashboardStats).mockResolvedValue({
      totalUsers: 100,
      activeUsers: 50,
      totalPosts: 200,
      totalComments: 500,
    });
  });

  it('redirects to login if not authenticated', async () => {
    // Ensure no token in localStorage
    localStorage.clear();
    
    render(
      <BrowserRouter>
        <DashboardPage />
      </BrowserRouter>
    );

    // Should redirect to login
    expect(mockNavigate).toHaveBeenCalledWith('/login');
  });

  it('displays loading state initially', () => {
    // Setup mock auth token
    localStorage.setItem('auth_token', 'test-token');
    
    render(
      <BrowserRouter>
        <DashboardPage />
      </BrowserRouter>
    );

    expect(screen.getByText('Loading dashboard...')).toBeInTheDocument();
  });

  it('renders dashboard with stats when data is loaded', async () => {
    // Setup mock auth token
    localStorage.setItem('auth_token', 'test-token');
    
    render(
      <BrowserRouter>
        <DashboardPage />
      </BrowserRouter>
    );

    // Wait for data to load
    await waitFor(() => {
      expect(screen.getByText('Welcome to your Dashboard')).toBeInTheDocument();
    });

    // Check that stats are displayed
    expect(screen.getByText('Total Users')).toBeInTheDocument();
    expect(screen.getByText('100')).toBeInTheDocument(); // Total users count
    expect(screen.getByText('Active Users')).toBeInTheDocument();
    expect(screen.getByText('50')).toBeInTheDocument(); // Active users count
    expect(screen.getByText('Total Posts')).toBeInTheDocument();
    expect(screen.getByText('200')).toBeInTheDocument(); // Total posts count
    expect(screen.getByText('Total Comments')).toBeInTheDocument();
    expect(screen.getByText('500')).toBeInTheDocument(); // Total comments count
  });

  it('shows error message when data fetch fails', async () => {
    // Setup mock auth token
    localStorage.setItem('auth_token', 'test-token');
    
    // Setup mock to reject with error
    vi.mocked(dashboardService.getDashboardStats).mockRejectedValue(
      new Error('Failed to fetch data')
    );
    
    render(
      <BrowserRouter>
        <DashboardPage />
      </BrowserRouter>
    );

    // Wait for error state
    await waitFor(() => {
      expect(screen.getByText('Failed to load dashboard data')).toBeInTheDocument();
    });

    // Check for retry button
    expect(screen.getByRole('button', { name: /retry/i })).toBeInTheDocument();
  });
}); 