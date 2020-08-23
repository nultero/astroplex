import Head from 'next/head'
import styles from '../styles/Home.module.css' // this is awesome modular css right here fam

export default function Home() {
  return (
    <div className={styles.container}>
      <Head>
        <title className='tinycaps'>Tᴀᴋᴇ ᴛʜᴇ Sᴛᴀʀs | astroplex</title>
        <link rel="icon" href="/favicon.ico" />
      </Head>

      <main>
        <h1 className='titlebar' >
          a<span className='titlebar2'>stroplex</span>
        </h1>

        <div className={styles.padding}>
        <p className='graph'>construction is still underway //</p>
        <p className='graph2'>please don't be alarmed</p>
        </div>
        
        
      </main>
    </div>
  )
}
