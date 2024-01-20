import React from 'react'

export default function Header() {
  return (
    <header>
        <div className='container'>
            <span className='logo'>LendMe</span>
            <ul className='nav'>
                <li className='nav_item'>Вход и регистрация</li>
                <li className='advertise'>Разместить объявление</li>
            </ul>

        </div>
        <div className='presentation'></div>
    </header>
  )
}
