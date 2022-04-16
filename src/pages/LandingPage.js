import '../App.css';
import { Button } from 'antd';

const LandingPage = () => {
    return (
        <div>
            <h1>Soundalike</h1>
                <p>
                    Soundalike recommends songs using the Million Song Challenge Dataset. It uses a recommender
                    system to create a curated playlist for any user. 
                </p>
            <Button type="primary">Begin</Button>
        </div>
    )
}

export default LandingPage;