

var initialState = {
    cnt: 2,
};

export default function mainReducer(state=initialState, action) {
    switch (action.type) {
    case 'CHANGE_COUNT':
        return Object.assign({}, state,
                             {
                                 cnt: action.new_cnt + state.cnt
                             });
    default:
        return state;
    }
}
