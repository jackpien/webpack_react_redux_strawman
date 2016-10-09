import React from 'react';
import {render} from 'react-dom';
import {createStore} from 'redux'
import {Provider} from 'react-redux'

import Counter from './Counter.jsx';
import Display from './Display.jsx';
import mainReducer from './reducers.js';

var store = createStore(mainReducer);

class App extends React.Component {
    render() {
        return(
                <div><p>Hi Webpack!</p><Counter nnn="jack"/>
                <Display/>
                </div>
                
        );
    }
}

render(<Provider store={store}>
       <App/>
       </Provider>,
       document.getElementById('app')
      );
