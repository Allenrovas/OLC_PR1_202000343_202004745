import axios from 'axios';

const instance = axios.create(
    {
        baseURL: 'http://3.140.207.88:4000/',
        timeout : 15000,
        headers: {
            'Content-Type': 'application/json',
        }
    }
);

export const reportes = async () => {
    const {data} = await instance.get('/reportes');
    return data;
}