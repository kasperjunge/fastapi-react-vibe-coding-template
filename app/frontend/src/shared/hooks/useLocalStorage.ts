import { useState, useEffect } from 'react';
import { safeJsonParse } from '@/shared/lib/utils';

/**
 * Custom hook to persist state in localStorage
 * @param key The localStorage key
 * @param initialValue The initial value (or function to get it)
 */
export function useLocalStorage<T>(
  key: string,
  initialValue: T | (() => T)
): [T, (value: T | ((prev: T) => T)) => void] {
  // Get stored value from localStorage or use initialValue
  const getStoredValue = (): T => {
    try {
      const item = localStorage.getItem(key);
      
      // Return parsed stored json or initialValue
      if (item) {
        return safeJsonParse<T>(item, getInitialValue());
      }
      
      return getInitialValue();
    } catch (error) {
      console.error('Error reading from localStorage:', error);
      return getInitialValue();
    }
  };

  // Get the initial value (handle function or direct value)
  const getInitialValue = (): T => {
    return initialValue instanceof Function ? initialValue() : initialValue;
  };

  // State to store our value
  const [storedValue, setStoredValue] = useState<T>(getStoredValue);

  // Return a wrapped version of useState's setter function that 
  // persists the new value to localStorage
  const setValue = (value: T | ((prev: T) => T)) => {
    try {
      // Allow value to be a function (like useState setter)
      const valueToStore = value instanceof Function ? value(storedValue) : value;
      
      // Save state
      setStoredValue(valueToStore);
      
      // Save to localStorage
      localStorage.setItem(key, JSON.stringify(valueToStore));
      
      // Dispatch a custom event so other hooks with the same key can update
      window.dispatchEvent(
        new CustomEvent('local-storage', { detail: { key, value: valueToStore } })
      );
    } catch (error) {
      console.error('Error saving to localStorage:', error);
    }
  };

  // Update the stored value if the key changes
  useEffect(() => {
    setStoredValue(getStoredValue());
  }, [key]);

  // Listen for changes across components/tabs
  useEffect(() => {
    const handleStorageChange = (e: StorageEvent) => {
      if (e.key === key && e.newValue) {
        setStoredValue(safeJsonParse(e.newValue, storedValue));
      }
    };

    const handleCustomStorageChange = (e: CustomEvent<{ key: string; value: T }>) => {
      if (e.detail.key === key) {
        setStoredValue(e.detail.value);
      }
    };

    // Listen for changes in other tabs/windows
    window.addEventListener('storage', handleStorageChange);
    
    // Listen for changes within the same tab
    window.addEventListener(
      'local-storage', 
      handleCustomStorageChange as EventListener
    );

    return () => {
      window.removeEventListener('storage', handleStorageChange);
      window.removeEventListener(
        'local-storage', 
        handleCustomStorageChange as EventListener
      );
    };
  }, [key, storedValue]);

  return [storedValue, setValue];
} 