import styles from '../styles/homelink.module.css';


export default function Homelink() {
  return (
    <div className={styles.container}>
        <h1 className={styles.homebar}><a href='/'>
            <span className={styles.homebarBorder}>
            <span className={styles.homebarMeteorAnchor}>
              </span>A</span>
              <span className={styles.homebarRed}>stroplex</span></a>
            </h1>
    </div>
  )
}