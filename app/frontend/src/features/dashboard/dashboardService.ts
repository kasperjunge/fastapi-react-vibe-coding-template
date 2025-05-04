import { sleep } from '@/shared/lib/utils';

export interface DashboardStats {
  totalUsers: number;
  activeUsers: number;
  totalPosts: number;
  totalComments: number;
}

export interface RecentActivity {
  id: string;
  type: 'post' | 'comment' | 'like';
  user: {
    id: string;
    name: string;
    avatar?: string;
  };
  content: string;
  timestamp: string;
}

export const dashboardService = {
  /**
   * Get dashboard statistics
   */
  getDashboardStats: async (): Promise<DashboardStats> => {
    try {
      // In a real app, this would call the API
      // return await api.get<DashboardStats>('/dashboard/stats');
      
      // For demo purposes, we'll simulate an API call
      await sleep(800);
      
      return {
        totalUsers: 120,
        activeUsers: 42,
        totalPosts: 328,
        totalComments: 1423,
      };
    } catch (error) {
      console.error('Error fetching dashboard stats:', error);
      throw new Error('Failed to load dashboard statistics');
    }
  },

  /**
   * Get recent activity feed
   */
  getRecentActivity: async (): Promise<RecentActivity[]> => {
    try {
      // In a real app, this would call the API
      // return await api.get<RecentActivity[]>('/dashboard/activity');
      
      // For demo purposes, we'll simulate an API call
      await sleep(600);
      
      return [
        {
          id: '1',
          type: 'post',
          user: {
            id: 'user1',
            name: 'John Doe',
          },
          content: 'Created a new post: "Getting Started with React"',
          timestamp: new Date(Date.now() - 5 * 60000).toISOString(),
        },
        {
          id: '2',
          type: 'comment',
          user: {
            id: 'user2',
            name: 'Jane Smith',
          },
          content: 'Commented on "TypeScript Tips and Tricks"',
          timestamp: new Date(Date.now() - 25 * 60000).toISOString(), 
        },
        {
          id: '3',
          type: 'like',
          user: {
            id: 'user3',
            name: 'Mike Johnson',
          },
          content: 'Liked "Building Modern UIs with Tailwind"',
          timestamp: new Date(Date.now() - 120 * 60000).toISOString(),
        },
      ];
    } catch (error) {
      console.error('Error fetching recent activity:', error);
      throw new Error('Failed to load recent activity');
    }
  },
}; 