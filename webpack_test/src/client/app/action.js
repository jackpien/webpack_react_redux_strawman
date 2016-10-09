export function changeCount(newCnt) {
    return {
        type: 'CHANGE_COUNT',
        new_cnt: newCnt,
    };
}

export function displayClick() {
    return {
        type: 'CHANGE_COUNT',
        new_cnt: 100,
    };
}
    
