import { Input } from 'antd';
import axios from 'axios'

const InputPage = () => {
    const { Search } = Input;
    const DEPLOYED_URL = 'https://soundalike2.vercel.app/flask/search';
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
        <div>
            <h3>Search for a song in the Million Song Database </h3>
            <Search
                placeholder="Search for a song"
                enterButton="Search"
                size="large"
                onSearch={onSearch}
            />
        </div>
    )
};

export default InputPage;