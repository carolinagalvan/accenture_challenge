import React from 'react'
import Head from 'next/head'
import Plates from '../pages/Plates'

const Home = () => (
  <div>
    <Head>
      <title>Home</title>
      <link rel='icon' href='/favicon.ico' />
      <link
        rel="stylesheet"
        href="https://maxcdn.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css"
        integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T"
        crossOrigin="anonymous"
      />
    </Head>

    <div className="hero">
      <h1 className="display-4">Smart Parking</h1>
    </div>

    <Plates></Plates>

    <style jsx>{`
      .hero {
        width: 100%;
        color: #333;
        text-align: center;
        margin-top: 30px;
      }
    `}</style>
  </div>
)

export default Home
