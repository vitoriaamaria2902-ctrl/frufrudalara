{
    margin:0;
    padding:0;
    box-sizing:border-box;
    font-family: Arial, sans-serif;
}

body{
    background:#EDE7DB;
    padding:20px;
}

/* lOGIN */
.login{
    max-width:400px;
    margin:auto;
    background:#EDE7DB;
    padding:30px;
    border-radius:25px;
}

.login h1{
    text-align:center;
    color:#F58B96;
    margin-bottom:30px;
}

form{
    display:flex;
    flex-direction:column;
}

label{
    margin:10px 0 5px;
}

input{
    padding:12px;
    border:2px solid #d89a42;
    border-radius:20px;
    background:#f0ddbb;
}

button{
    margin-top:15px;
    padding:14px;
    border-radius:25px;
    font-size:18px;
    cursor:pointer;
}

.entrar{
    background:#F58B96;
    color:white;
    border:none;
}

.cadastro{
    background:transparent;
    border:2px solid #2f7d32;
    color:#2f7d32;
}

form a{
    text-align:center;
    margin-top:15px;
    color:black;
}

/* produtos */
.produtos{
    max-width:420px;
    margin:40px auto;
    background:#EDE7DB;
    border-radius:25px;
    overflow:hidden;
}

.topo{
    display:flex;
    align-items:center;
    gap:15px;
    padding:20px;
}

.topo h2{
    color:#F58B96;
}

.menu{
    font-size:24px;
}

.busca{
    padding:0 20px 15px;
}

.busca input{
    width:100%;
    border:none;
    background:white;
}

nav{
    background:#F6C7C7;
    display:flex;
    justify-content:space-around;
    padding:12px;
}

nav a{
    text-decoration:none;
    color:black;
}

main{
    padding:20px;
}

h3{
    margin:20px 0;
}

.destaques{
    display:flex;
    gap:15px;
}

.destaques div{
    width:90px;
    height:70px;
    background:#ddd;
    border-radius:10px;
}

.produtos{
    display:grid;
    grid-template-columns:1fr 1fr;
    gap:20px;
}

.produtos div{
    height:120px;
    background:#ddd;
}



