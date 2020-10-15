import { Container } from '@material-ui/core';
import Head from 'next/head';
import styles from '../styles/projects.module.css';


export default function Index() {

  function head() {
    let headray = ['Wᴀᴛᴇʀᴍᴇʟᴏɴs'];
    return headray[0];
  }

  return (
    <Container maxWidth='sm'>
    <div className={styles.container}>
      <Head>
        <title className='tinycaps'>{head()} | astroplex</title>
        <link rel="icon" href="/favicon.ico" />
      </Head>

      <main>
        <h1 className={styles.titlebar} >
          P<span className={styles.titlebarRed}>rojects</span>
        </h1>

        <div className={styles.padding}>
        <h3 className={styles.graphLink}> <a href='/projects/devilscrypt'>{">>"} Devilscrypt {">>"}</a></h3>
        </div>
        
        
      </main>
    </div>
    </Container>
  )
}