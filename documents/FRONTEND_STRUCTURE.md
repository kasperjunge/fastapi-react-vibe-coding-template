## Modern React Project Structure Documentation

### Overview

The project follows a modern React application structure using Vite as the build tool, TypeScript for type safety, and a component-based architecture. The application uses React Router for routing, React Query for data fetching, and Tailwind CSS with Shadcn UI components for styling. As the application grows, a **feature-first folder grouping** is adopted to keep related code co-located. Each feature now includes its own tests directory to improve discoverability and maintainability.

### File Tree (with Co‑located Tests)

```plain
project-root/
├── public/                 # Minimal static files (favicon, index.html)
│   └── index.html
├── src/                    # Source code
│   ├── assets/             # Static assets (images, icons, fonts)
│   │   ├── icons/
│   │   ├── images/
│   │   └── fonts/
│   ├── features/           # Feature-first modules
│   │   ├── dashboard/
│   │   │   ├── DashboardPage.tsx
│   │   │   ├── dashboardService.ts
│   │   │   ├── hooks.ts
│   │   │   ├── Dashboard.components.tsx
│   │   │   ├── images/     # Feature-scoped assets
│   │   │   └── __tests__/  # Co-located unit tests
│   │   │       └── DashboardPage.test.tsx
│   │   ├── auth/
│   │   │   ├── LoginPage.tsx
│   │   │   ├── authService.ts
│   │   │   ├── AuthContext.tsx
│   │   │   ├── icons/
│   │   │   └── __tests__/
│   │   │       └── LoginPage.test.tsx
│   │   └── ...             # Other features with __tests__ directories
│   ├── shared/             # Reusable code across features
│   │   ├── ui/             # Shadcn UI components
│   │   ├── lib/            # Utility functions
│   │   ├── services/       # API services and external integrations
│   │   └── types/          # Shared TypeScript types
│   ├── App.tsx             # Main app component (routing, providers)
│   ├── main.tsx            # React bootstrap entry point
│   ├── index.css           # Global styles (Tailwind base)
│   ├── vite-env.d.ts       # Vite TypeScript declarations
│   └── vite.config.ts      # Vite configuration
├── .gitignore
├── components.json
├── eslint.config.js
├── package.json
├── postcss.config.js
├── tailwind.config.ts
├── tsconfig.json
├── tsconfig.app.json
└── tsconfig.node.json
```

### Key Directory Responsibilities

* **`src/assets/`**: Static files (images, icons, fonts) for direct imports—optimized by Vite. Discipline around import size is assumed.
* **`src/features/`**: Each feature folder is self-contained: pages, components, hooks, services, assets, and now tests. This co-location reduces cognitive load and keeps implementation and verification side-by-side.
* **`src/shared/ui/`**, **`shared/lib/`**, **`shared/services/`**, and **`shared/types/`**: Unchanged—centralized, reusable code.

### Co‑located Tests

By moving feature tests into `__tests__` folders under each feature:

1. **Discoverability**: Tests live next to the code they verify, reducing context switching.
2. **Maintainability**: As features evolve, test files travel with implementation files.
3. **Isolation**: CI configurations can target `**/__tests__/**/*.test.tsx`, keeping scope clear.

### Architecture Patterns & Best Practices

All patterns (Component Architecture, Routing, State Management, Data Layer, Styling) remain as before. Co‑located tests augment your workflow by providing immediate feedback within each feature module.