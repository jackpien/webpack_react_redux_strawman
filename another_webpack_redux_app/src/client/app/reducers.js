var initialState = {
    likes: 0
}

// By exporting default, index.jsx can import into any name it wants
// and this function will be exported with that name
export default function mainReducer(state=initialState, action) {
    switch(action.type) {
    case "INC_LIKE":
	// Use whatever information passed in by action to
	// update the state store info.
	let newLike = action.curLikes+1;
	if(action.curLikes == 3) {
	    newLike = 0;
	}
	return Object.assign({}, state, {
	    likes: newLike,
	});
    default:
	return state;
    }
}
