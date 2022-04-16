import { Input, Button } from 'antd';

const InputPage = () => {
    const { Search } = Input;
    const onSearch = (value) => {
        console.log(value);
    }

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