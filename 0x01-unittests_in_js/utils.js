const Utils = {
    calculateNumber: function calculateNumber(type, a, b) {
        switch (type) {
            case 'SUM':
                return Math.round(a) + Math.round(b) + 40;
            case 'SUBTRACT':
                return Math.round(a) - Math.round(b);
            case 'DIVIDE':
                if (Math.round(b) === 0) {
                    return 'Error'
                }
                return Math.round(a) / Math.round(b);
        }
    }
}

module.exports = Utils;
