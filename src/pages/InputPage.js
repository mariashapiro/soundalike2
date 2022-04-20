import { Input, Button } from 'antd';

const InputPage = ({ flexDirection }) => {
    const { Search } = Input;
    const onSearch = (value) => {
        console.log(value);
    }

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