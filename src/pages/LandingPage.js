import '../App.css';
import { Button } from 'antd';
import { Link } from 'react-router-dom';


const LandingPage = ({ flexDirection }) => {
    return (
        <div className="page" style={{ flexDirection: flexDirection }}>
            <div>
                <h1>Soundalike</h1>

                <p>
                    Soundalike recommends songs using the Million Song Challenge Dataset. It uses a recommender system to create a curated playlist for any user.
                </p>
                <p className='italics'>scroll</p>


            </div>
        </div>
    );
};

export default LandingPage;