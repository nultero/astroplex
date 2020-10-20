import { Link } from '@material-ui/core';
import styles from '../styles/homelink.module.css';


export default function Homelink() {
  return (
    <div className={styles.container}>
        <h1 className={styles.homebar}><Link href='/'>
            <span className={styles.homebarBorder}>
            <span className={styles.homebarMeteorAnchor}>
              </span><span id={styles.homelinker}>A</span></span>
              <span className={styles.homebarRed}>stroplex</span></Link>
            </h1>
    </div>
  )
}