import React, {Component} from 'react';

export class Exercise1 extends Component {
  constructor(props) {
    super(props);
    this.state = {
      alphabet: 'abcdefghijklmnopqrstuvwxyz'
    };
  }
  
  render() {
    const {alphabet} = this.state;

    return (
      <div className="container">
        Alphabet
        <ul>
          {
            alphabet.split('').map((element, i) => 
              <li key={i}>
                {`${element}${alphabet}`.substring(i + 1, alphabet.length + 1) + `${alphabet}`.substring(0, i)}
              </li>
            )
          }
        </ul>
      </div>
    );
  }
}

export default Exercise1;
