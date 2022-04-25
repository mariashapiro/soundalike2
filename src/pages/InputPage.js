import { Input } from 'antd';
import axios from 'axios'
import React, { useState } from 'react';

const InputPage = ({ flexDirection }) => {
    const { Search } = Input;
    const DEPLOYED_URL = 'https://soundalike2.vercel.app/flask/search'; //use when deploying
    const DEV_URL = 'http://127.0.0.1:5000/flask/search';

    const [recSongs, setRecSongs] = useState([]);
    const [recSongMetrics, setRecSongMetrics] = useState([]);
    const SUGGESTED_SONGS = [
        "Hey Ya! by Outkast",
        "Finding Myself by Smile Empty Soul",
        "Soma by The Strokes",
        "Smells Like Nirvana by Weird Al Yankovic",
        "California Love by 2pac",
        "The Invisible Man by Michael Cretu",
    ];

    const onSearch = (value) => {
        axios.post(DEV_URL, {
            song_title: value
        }, {

        }).then(response => {
            console.log('success', response)
            setRecSongs(response.data.rec_songs);
            setRecSongMetrics(response.data.rec_song_metrics);
            console.log('recSongs ', recSongs);
        }).catch(error => {
            console.log('error', error)
            setRecSongs([]);
            setRecSongMetrics([]);
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

                    {recSongs.length > 0 ?
                        <div className='grid-container'>
                            <div className='grid-child'>
                                <h2>Recommended Songs</h2>
                                <ul>
                                    {recSongs.map(function (item) {
                                        return <li key={item}>{item}</li>
                                    })}
                                </ul>
                            </div>
                            <div className='grid-child'>
                                <h2>Song Similarity Score</h2>
                                <ul>
                                    {recSongMetrics.map(function (item) {
                                        return <li key={item}>{item}</li>
                                    })}
                                </ul>
                            </div>
                        </div>
                        :
                        <div>
                            <h2>Try one of these songs!</h2>
                            <ul>
                                {SUGGESTED_SONGS.map(function (item) {
                                        return <li key={item}>{item}</li>
                                    })}
                                </ul>
                        </div>
                    }
                </div>

            </div>
            <div className="footer">
                <p>
                    Technologies used: React, Flask, Python, Million Song Dataset (subset)
                </p>
                <p>
                    This website is our final project on recommender systems for Spring 2022 CS4675 at Georgia Tech under professor Dr. Ling Liu.
                </p>
            </div>
        </div>

    );
};

export default InputPage;