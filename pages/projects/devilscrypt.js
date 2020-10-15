import { Container } from '@material-ui/core';
import React, { Component } from 'react';
import Head from 'next/head';
import Homelink from '../../components/homelink';
import styles from '../../styles/devilscrypt.module.css';
import cipher from '../../data/cipher.json';

class DevilScrypt extends Component {  

  constructor(props) {
    super(props);
    this.updatesChange = this.updatesChange.bind(this);
    this.cipherRender = this.cipherRender.bind(this);
    this.cipher = cipher;
    this.fault = `${this.cipher[0]}`;
    this.topString = `evilScrypt`;
    this.state = { topString: this.topString, string: this.fault,
                    };
}

  updatesChange(evt) {
    this.setState({ 
      string: evt.target.values,
    });
  }

  topbar(ebb, ebbstate) {
    const topS = `evilScrypt`;
    let newState = ``;
    for (let i = 0; i < topS.length; i++) {
      if (i !== ebbstate) {
        newState = newState + topS[i];
      }
      else if (i === ebbstate) {
        newState = newState + cipher[ebb];
      }
    }

    this.setState({
     topString: `${newState}`,
    })
  }

  componentDidMount() { 
    let nextinterval = Math.floor(Math.random() * 9000);
    setInterval(() => {
      let ebb = Math.floor(Math.random() * 63);
      let ebbstate = Math.floor(Math.random() * 9);
      nextinterval = Math.floor(Math.random() * 9000);
      this.topbar(ebb, ebbstate);
    }, nextinterval);
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

        <Homelink />

        <div className={styles.titlediv}>
          <h1 className={styles.titlebar} >
            <span className={styles.titlebarBorder}>D</span><span className={styles.titlebarRed}>{this.state.topString}</span>
          </h1>
        </div>
          <textarea className={styles.devilbox} onChange={this.updatesChange} value={this.cipherRender()}  ></textarea>
          <p className={styles.fontismQuick}>{`Yello`}</p>

        </main>
        </div>
    </Container>
     );
   };
 }
 
 export default DevilScrypt;