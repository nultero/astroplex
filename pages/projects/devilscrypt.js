import { Container } from '@material-ui/core';
import React, { Component } from 'react';
import Head from 'next/head';
import styles from '../../styles/devilscrypt.module.css';
import cipher from '../../data/cipher.json';

class DevilScrypt extends Component {  

  constructor(props) {
    super(props);
    this.updatesChange = this.updatesChange.bind(this);
    this.cipherRender = this.cipherRender.bind(this);
    this.cipher = cipher;
    this.fault = `${this.cipher[0]}`;
    this.topString = `${this.cipher[0]}`;
    this.state = { topString: this.topString, string: this.fault };
}

  updatesChange(evt) {
    this.setState({ 
      string: evt.target.values,
    });
  }

  componentDidMount() {  
   this.setState({
    topString: `${this.cipher[0]}`,
   })
  }

  cipherRender() {
    let ren = [];
    let i = 0;
    while (i < 60) {
        ren.push(this.cipher[i]);
        i++;
    }
    return ren;
  }



  render() {

      return (
        <Container maxWidth='sm'>
        <div className={styles.container}>
        <Head>
          <title className='tinycaps'>Eʏᴇʙᴀʟʟ Pɪᴇ | astroplex</title>
          <link rel="icon" href="/favicon.ico" />
        </Head>

        <main>
        <h1 className={styles.titlebar} >
          <span className={styles.titlebarBorder}>D</span><span className={styles.titlebarRed}>evilScrypt</span>
        </h1>
          <textarea className={styles.devilbox} onChange={this.updatesChange} value={this.cipherRender()}  ></textarea>
          {/* <p className={styles.fontism}>{this.cipherRender()}</p> */}
        </main>
        </div>
    </Container>
     );
   };
 }
 
 export default DevilScrypt;