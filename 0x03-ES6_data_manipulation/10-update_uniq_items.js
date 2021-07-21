export default function updateUniqueItems(mappy) {
  if (!(mappy instanceof Map)) {
    throw new Error('Cannot process');
  }
  mappy.forEach((value, key, map) => {
    if (value === 1) {
      map.set(key, 100);
    }
  });
  return mappy;
}
