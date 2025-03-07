import './home.css'
import { Button,Descriptions,Avatar,Space } from 'antd';
import { UserOutlined } from '@ant-design/icons';
import { useNavigate } from "react-router";

export default function Home() {
  let navigate = useNavigate();
  const StudyItem = [
    {
      name: '多邻国',
      content:[
        {
          key: '1',
          label: '单词',
          children: '100',
        },
        {
          key: '2',
          label: '句子',
          children: '200',
        },
        {
          key: '3',
          label: '笔记',
          children: '200',
        },
        {
          key: '4',
          label: '疑问',
          children: '10/200',
        },
      ]
    },
    {
      name: '新标日',
      content:[
        {
          key: '1',
          label: '单词',
          children: '100',
        },
        {
          key: '2',
          label: '句子',
          children: '200',
        },
        {
          key: '3',
          label: '笔记',
          children: '200',
        },
        {
          key: '5',
          label: '疑问',
          children: '10/200',
        },
      ]
    },
  ]
  const goToAddPage = () => {
    navigate("/add");
  }
  return <div>
     <Space
      direction="vertical"
      size="middle"
      style={{
        display: 'flex',
      }}
    >
    <div><Avatar size={30} icon={<UserOutlined />} className='margin-right-10' />王ちゃん</div>
    {
      StudyItem.map(item => (
        <Descriptions
          bordered
          title={item.name}
          size="small"
          extra={<div>
            <Button type="primary" size='small' className='margin-right-10' onClick={() => goToAddPage()}>添加</Button>
            <Button type="primary" size='small'>复习</Button>
          </div>}
          items={item.content}
        />
      ))
    }
    
    </Space>
  </div>
}