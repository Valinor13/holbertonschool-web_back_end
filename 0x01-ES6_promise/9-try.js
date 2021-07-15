export default function guardrail(mathFunction) {
  const queue = [];
  mathFunction.then((value) => queue.push(value, 'Guardrail was processed'));
  return queue;
}
