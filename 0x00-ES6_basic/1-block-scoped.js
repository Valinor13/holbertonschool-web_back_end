#!/usr/bin/node

export default function taskBlock(trueOrFalse) {
    task = false;
    task2 = true;

    if (trueOrFalse) {
        let task = true;
        let task2 = false;
    }

    return [task, task2];
}
