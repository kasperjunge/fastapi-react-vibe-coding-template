import { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { Button } from '@/shared/ui/button';
import { dashboardService } from './dashboardService.ts';

type DashboardStats = {
  totalUsers: number;
  activeUsers: number;
  totalPosts: number;
  totalComments: number;
};

export default function DashboardPage() {
  const navigate = useNavigate();
  const [stats, setStats] = useState<DashboardStats | null>(null);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    // Check if user is authenticated
    const token = localStorage.getItem('auth_token');
    if (!token) {
      navigate('/login');
      return;
    }

    // Fetch dashboard data
    const fetchData = async () => {
      try {
        setIsLoading(true);
        const data = await dashboardService.getDashboardStats();
        setStats(data);
      } catch (err: any) {
        console.error('Failed to fetch dashboard data:', err);
        setError(err?.message || 'Failed to load dashboard data');
      } finally {
        setIsLoading(false);
      }
    };

    fetchData();
  }, [navigate]);

  const handleLogout = () => {
    localStorage.removeItem('auth_token');
    navigate('/login');
  };

  if (isLoading) {
    return (
      <div className="flex h-screen items-center justify-center">
        <div className="text-xl">Loading dashboard...</div>
      </div>
    );
  }

  if (error) {
    return (
      <div className="flex h-screen flex-col items-center justify-center gap-4">
        <div className="text-xl text-destructive">{error}</div>
        <Button onClick={() => window.location.reload()}>Retry</Button>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-background">
      {/* Header */}
      <header className="border-b border-border bg-card shadow-sm">
        <div className="container mx-auto flex h-16 items-center justify-between px-4">
          <div className="text-2xl font-bold">Dashboard</div>
          <Button variant="outline" onClick={handleLogout}>
            Logout
          </Button>
        </div>
      </header>

      {/* Main content */}
      <main className="container mx-auto px-4 py-8">
        <h1 className="mb-6 text-3xl font-bold">Welcome to your Dashboard</h1>

        {/* Stats Cards */}
        <div className="grid grid-cols-1 gap-6 md:grid-cols-2 lg:grid-cols-4">
          <div className="rounded-lg border border-border bg-card p-6 shadow-sm">
            <h3 className="mb-2 text-lg font-medium text-muted-foreground">Total Users</h3>
            <p className="text-3xl font-bold">{stats?.totalUsers || 0}</p>
          </div>
          
          <div className="rounded-lg border border-border bg-card p-6 shadow-sm">
            <h3 className="mb-2 text-lg font-medium text-muted-foreground">Active Users</h3>
            <p className="text-3xl font-bold">{stats?.activeUsers || 0}</p>
          </div>
          
          <div className="rounded-lg border border-border bg-card p-6 shadow-sm">
            <h3 className="mb-2 text-lg font-medium text-muted-foreground">Total Posts</h3>
            <p className="text-3xl font-bold">{stats?.totalPosts || 0}</p>
          </div>
          
          <div className="rounded-lg border border-border bg-card p-6 shadow-sm">
            <h3 className="mb-2 text-lg font-medium text-muted-foreground">Total Comments</h3>
            <p className="text-3xl font-bold">{stats?.totalComments || 0}</p>
          </div>
        </div>

        {/* Recent Activity Section */}
        <section className="mt-12">
          <h2 className="mb-4 text-2xl font-bold">Recent Activity</h2>
          <div className="rounded-lg border border-border">
            <div className="p-6 text-center text-muted-foreground">
              No recent activity to display.
            </div>
          </div>
        </section>
      </main>
    </div>
  );
} 