import { Container } from '@material-ui/core';
import React, { Component } from 'react';
import Head from 'next/head';
import Homelink from '../../components/homelink';
import styles from '../../styles/sipherglyph.module.css';
import cipher from '../../data/cipher.json';
import uncipher from '../../data/uncipher.json';


class SipherGlyph extends Component {  

  constructor(props) {
    super(props);
    this.checker = this.checker.bind(this);
    this.copyClip = this.copyClip.bind(this);
    this.crypt = this.crypt.bind(this);
    // this.postcall = this.postcall.bind(this);
    this.randomize = this.randomize.bind(this);
    this.reset = this.reset.bind(this);
    this.cipher = cipher;
    this.uncipher = uncipher;
    this.isCiphered = false;
    this.isPlainText = false;
    this.chars = ` abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*():"'<>?[],.?/-_=+\n\`~;`;
    this.defaultString = 'paste ciphertext or write a message to be encrypted here';
    this.primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149]
    this.max = this.primes.length;
    this.primesPick = [];
    this.sipherglyph = '<< placeholder >>';
    this.scrypt = 'paste ciphertext or write a message to be encrypted here';
    this.textMonkey = `textmonkey does not feel like dealing with whatever you've done in the box`;
    this.topString = `ipherGlyph`;
    this.state = { topString: this.topString, scrypt: this.scrypt,
                   sipherglyph: this.sipherglyph, primesPick: this.primesPick };
}

  randomize(max) {
    let rand = Math.floor(Math.random() * max);
    return rand;
  }
  reset() {
    this.isCiphered = false;
    this.isPlainText = false;
  }

  checker(text) {
    for (let i = 0; i < text.length; i++) {
      if (this.chars.includes(text[i]) == true) {
        this.isPlainText = true;
        // console.log(`is plain text == ${this.isPlainText}`)
      }
      else if (this.chars.includes(text[i]) == false) {
        this.isCiphered = true;
        // console.log(`is ciph == ${this.isCiphered}`)
    }}}

  crypt(event) {
    this.scrypt = event.target.value;
    this.reset();
    if (0 < this.scrypt.length <= 100) {
      this.checker(this.scrypt);
      this.sipherglyph = ``;
      
      for (let i = 0; i < this.scrypt.length; i++) {        
        if (this.isCiphered === false && this.isPlainText === true) { //only plaintext
          this.sipherglyph = this.sipherglyph + this.cipher[this.uncipher[this.scrypt[i]]] + this.cipher[151];
          // this.sipherglyph = this.sipherglyph + this.cipher[this.uncipher[this.scrypt[i]]] + this.uncipher[this.scrypt[i]] + this.cipher[151];
        }
        else if (this.isPlainText === false && this.isCiphered === true) { // only ciphertext
          this.sipherglyph = ``;
          console.log(`not ready yet`);
        }
        else { // both ciphertext and plaintext / some random chars are in the textbox; do nothing
          this.sipherglyph = this.textMonkey;
        }
      }
      // post-processing function, method getting kinda bloated
      if (this.sipherglyph !== this.textMonkey && this.isCiphered === false) {
        let firstPrime = this.primes[this.randomize(this.max)];
        let secondPrime = this.primes[this.randomize(this.max)];
        let spliceVar = this.randomize(this.sipherglyph.length);
        this.sipherglyph = this.sipherglyph.substring(0, spliceVar) +
          this.cipher[151] + this.cipher[firstPrime] + this.cipher[150] + this.cipher[secondPrime] +
          this.cipher[151] + this.sipherglyph.substring(spliceVar);
      }}
      
    else if (this.scrypt.length > 100) {
      this.sipherglyph = `textbox has exceeded the length that I want to deal with`;
    }
      





    //
    //
    //
    //


    for (let i = 0; i < this.sipherglyph.length; i++) {        
      console.log(`${this.uncipher[this.scrypt[i]]} - ${this.cipher[this.uncipher[this.scrypt[i]]]}`)
    }

    // 
    // 
    // need precompiled reverse ciphers to debug 2 of my unicode chars not rendering
    // 
    // 
    // 














    this.setState({ 
      // scrypt: this.scrypt,    
      sipherglyph: this.sipherglyph,
    })
}





  topbar(ebb, ebbstate) {
    const topS = `ipherGlyph`;
    let newState = ``;
    for (let i = 0; i < topS.length; i++) {
      if (i !== ebbstate) {
        newState = newState + topS[i];
      }
      else if (i === ebbstate) {
        newState = newState + cipher[ebb];
      }}
    this.setState({
     topString: `${newState}`,
    })
  }

  componentDidMount() { 
    let nextinterval = 10000;
    setInterval(() => { 
      let ebb = this.randomize(150);
      let ebbstate = this.randomize(10);
      nextinterval = this.randomize(9000);
      this.topbar(ebb, ebbstate);
    }, nextinterval);
  }

  copyClip() { // I know this part is old school but I couldn't figure out the clipboard api lol
    let copier = document.querySelector("#darkbox");
    copier.select();
    document.execCommand("copy");
  }




















  // code is product of two primes
  // that dot (cipher[163]), the last one, is the breakpoint between the primes
  // in ciphertext, cipher will go ... 
  // 
  // 
  // 
  // 
  // string(includes)
  // 
  // 
  // 
  // 
  // 
  // 
  // 
  // 
  // 
  // 
  // 
  // 

























  render() {

      return (
        <Container maxWidth={'md'} disableGutters={true}>
        <div className={styles.container}>
        <Head>
          <title className='tinycaps'>( ͡° ͜ʖ ͡°( ͡❛ ㅅ ͡❛) ͡° ͜ʖ ͡°) | astroplex</title>
          <link rel="icon" href="/favicon.ico" />
        </Head>

        <main>

        <Homelink />

        <div className={styles.titlediv}>
          <h1 className={styles.titlebar} >
            <span className={styles.titlebarBorder}>S</span><span className={styles.titlebarRed}>{this.state.topString}</span>
          </h1>
        </div>
          <textarea className={styles.glyphbox} onChange={(event) => this.crypt(event)} placeholder={this.defaultString} ></textarea>
          <p className={styles.outputArrow}>{`↓`}</p>


          <p className={styles.fontismQuick}>{`output:`}</p>
          <textarea className={styles.glyphbox} id={'darkbox'} readOnly={true} value={this.state.sipherglyph} ></textarea>
          <button className={styles.copyButton} onClick={this.copyClip}>copy to clipboard</button>

        </main>
        </div>
    </Container>
     );
   };
 }
 
 export default SipherGlyph;