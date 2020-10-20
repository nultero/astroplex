import { Container } from '@material-ui/core';
import Head from 'next/head';
import Link from 'next/link';
import styles from '../styles/index.module.css'; // this is awesome modular css right here fam


export default function Index() {
  return (
    <Container maxWidth='sm'>
    <div className={styles.container}>
      <Head>
        <title className='tinycaps'>Tᴀᴋᴇ ᴛʜᴇ Sᴛᴀʀs | astroplex</title>
        <link rel="icon" href="/favicon.ico" />
      </Head>

      <main>
        <h1 className={styles.titlebar} >
        <span className={styles.titlebarBorder}>
        <span className={styles.titlebarMeteorAnchor}>
          </span>A</span>
          <span className={styles.titlebarRed}>stroplex</span>
        </h1>

        <div className={styles.padding}>
        <p className={styles.graph}>construction is still underway //</p>
        <h3 className={styles.graphLink}> <Link href='/projects'><a>{">>"} Projects {">>"}</a></Link></h3>
        </div>


      </main>
    </div>
    </Container>
  )
}
