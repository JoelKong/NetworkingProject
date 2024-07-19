export const getData = async () => {
  return (
    await fetch('/api/data', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      // TODO: Verify
      body: JSON.stringify({
        phone_numbers: []
      })
    })
  ).json();
};
