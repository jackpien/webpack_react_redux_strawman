// What we pass to reducers mainReducer function
// Pass in any state, substate info you think the reducer needs
// to update the state store
export function incLike(curLikes) {
    return {
	type: "INC_LIKE",
	curLikes: curLikes,
    }
}
