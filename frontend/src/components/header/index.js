import styles from './style.module.css'
import Container from '../container'
import { Nav, Logo } from '../index.js'

const Header = () => {
  return <header
    className={styles.header}
  >
    <Container>
    <div className={styles.headerContent}>
        <Logo />
        <Nav />
        <p>AccountMenu</p>
        <p>Search</p>
        <p>Location</p>
    </div>
    </Container>
  </header>
}

export default Header