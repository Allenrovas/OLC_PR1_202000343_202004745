import axios from 'axios';

const instance = axios.create(
    {
        baseURL: 'http://localhost:9000/',
        timeout : 15000,
        headers: {
            'Content-Type': 'application/json',
        }
    }
);

export const reportesc3d = async () => {
    const {data} = await instance.get('/reportesc3d');
    return data;
}