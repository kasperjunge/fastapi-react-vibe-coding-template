# Frontend

This is the frontend application built with React, TypeScript, and Tailwind CSS. It follows a feature-based folder structure and uses modern best practices.

## Features

- React 18 with TypeScript
- Vite for fast development and optimized production builds
- TanStack Query for data fetching
- React Router for navigation
- Tailwind CSS for styling
- Custom UI components with shadcn-inspired design
- Unit testing with Vitest and Testing Library

## Getting Started

### Prerequisites

- Node.js 18+
- npm or yarn

### Installation

```bash
# Install dependencies
npm install

# Start development server
npm run dev

# Build for production
npm run build

# Run tests
npm test
```

## Project Structure

```
frontend/
├── public/               # Static assets
├── src/
│   ├── app/              # App entry point and layout
│   ├── features/         # Feature-based modules
│   │   ├── auth/         # Authentication-related components
│   │   ├── dashboard/    # Dashboard-related components
│   │   └── ...other features
│   ├── shared/           # Shared code across features
│   │   ├── components/   # Shared UI components
│   │   ├── hooks/        # Custom React hooks
│   │   ├── lib/          # Utility functions
│   │   ├── services/     # API services and data fetching
│   │   ├── types/        # TypeScript type definitions
│   │   └── ui/           # UI component library
│   ├── main.tsx          # Application entry point
│   ├── App.tsx           # Main App component with routing
│   └── index.css         # Global styles
├── .eslintrc.js          # ESLint configuration
├── package.json          # Dependencies and scripts
├── postcss.config.js     # PostCSS configuration
├── tailwind.config.ts    # Tailwind CSS configuration
├── tsconfig.json         # TypeScript configuration
└── vite.config.ts        # Vite configuration
```

## Development Guidelines

### Component Creation

- Feature-specific components should be placed in their respective feature directory
- Shared UI components should go in `src/shared/ui`
- Use TypeScript interfaces for component props

### Styling

- Use Tailwind CSS classes for styling
- Use the `cn()` utility function for conditional class names

### API Requests

- Use the `api` service from `src/shared/services/api.ts` for making HTTP requests
- Create feature-specific service files in the respective feature directory

### Testing

- Place tests in `__tests__` directories within each feature
- Follow the testing patterns used in the existing tests 