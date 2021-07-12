#!/usr/bin/node

export default function taskBlock(trueOrFalse) {
    if (trueOrFalse) {
        task = true;
        task2 = false;
    }

    const task = false;
    const task2 = true;
    return [task, task2];
}
