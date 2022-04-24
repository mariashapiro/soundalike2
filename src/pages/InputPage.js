import { Input } from 'antd';
import axios from 'axios'

const InputPage = ({ flexDirection }) => {
    const { Search } = Input;
    const DEPLOYED_URL = 'https://soundalike2.vercel.app/flask/search'; //use when deploying
    const DEV_URL = 'http://127.0.0.1:5000/flask/search';

    const onSearch = (value) => {
        axios.post(DEV_URL, {
            song_title: value
        }, {
    
        }).then(response => {
            console.log('success', response)
        }).catch(error => {
            console.log('error', error)
        });

    };

    return (
        <div >
            <div className="page" style={{ flexDirection: flexDirection }}>
                <div>
                    <h1>Search for a song in the Million Song Database </h1>

                    <Search
                        placeholder="Search for a song"
                        enterButton="Search"
                        size="large"
                        onSearch={onSearch}
                    />
                </div>

            </div>
            <div className="footer">
                <p>
                    Technologies used: React, Vercel, Flask, Python, Million Song Dataset (subset)
                </p>
                <p>
                    This website is our final project on recommender systems for Spring 2022 CS4675 at Georgia Tech under professor Dr. Ling Liu.
                </p>
            </div>
        </div>

    );
};

export default InputPage;