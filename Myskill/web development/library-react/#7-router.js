```
        React Router
        

        1. add react router
        ketika membuat apk create-react-app, belum ada page routing. react router akan jadi solusi untuk ini.

        ketik ini diterminal:
        - masuk ke folder react-router
        - ketik npm i -D react-router-dom
          atau...
          npm i -D react-router-dom@latest



        2. Folder Structure

        react-router
            src
                pages
                - layout.js
                - home.js
                - blogs.js
                - contact.js
                - nopage.js


        3. Add router in our App.js
            1. menambahkan routing pada app.js



```

// add router in App.js
<BrowserRouter>
        <Routes>
            <Router path="/" element={<Layout/>}>
                <Router index element={<Home/>} />
                <Router path="blogs" element={<Blogs/>} />
                <Router path="contact" element={<Contact/>} />
                <Router path="path" element={<NoPage/>} />
            </Router>
        </Routes>
</BrowserRouter>




// 