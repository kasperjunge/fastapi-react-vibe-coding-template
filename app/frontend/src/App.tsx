import { Route, Routes } from 'react-router-dom';
import { lazy, Suspense } from 'react';

// Lazy load feature pages
const DashboardPage = lazy(() => import('./features/dashboard/DashboardPage'));
const LoginPage = lazy(() => import('./features/auth/LoginPage'));

function App() {
  return (
    <Suspense fallback={<div className="flex h-screen items-center justify-center">Loading...</div>}>
      <Routes>
        <Route path="/login" element={<LoginPage />} />
        <Route path="/" element={<DashboardPage />} />
        <Route path="*" element={<div>Not Found</div>} />
      </Routes>
    </Suspense>
  );
}

export default App; 