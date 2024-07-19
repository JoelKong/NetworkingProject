export const activateSensors = () => {
  return fetch('/api/activate', {
    method: 'PUT'
  });
};
