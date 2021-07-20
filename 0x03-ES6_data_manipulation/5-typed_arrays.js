/* eslint-disable no-unused-vars */
export default function createInt8TypedArray(length, position, value) {
  if (position >= length) {
    throw new Error('Position outside of range');
  }
  const a = new ArrayBuffer(length);
  const view = new DataView(a);
  view.setUint8(position, value);
  return view;
}
