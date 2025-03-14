import './home.css'
import { Button,Table,Avatar,Space } from 'antd';
import { UserOutlined } from '@ant-design/icons';
import { useNavigate } from "react-router";
import React, {useEffect, useState} from 'react';
import { getSourceList } from '../../api/index';

export default function Home() {
  let navigate = useNavigate();
  const [studyItems, setStudyItems] = useState([])
  const columns = [
    {
      title: '来源',
      dataIndex: 'source_type_name',
      key: 'source_type_name',
    },
    {
      title: '单词',
      dataIndex: 'word_count',
      key: 'word_count',
    },
    {
      title: '操作',
      dataIndex: 'operate',
      key: 'operate',
      render: (_, record) => (
        <Space size="middle">
          <Button type="primary" size='small' onClick={() => goToAddPage(record)}>添加</Button>
          <Button type="primary" size='small'>复习</Button>
        </Space>
      ),
    },
  ];
  const goToAddPage = () => {
    navigate("/add");
  }
  const getSourceListFn = () => {
    getSourceList({}).then(res => {
      if(res.code == 200) {
        let data = res.data || [];
        setStudyItems(data)
      }
    })
  }
  useEffect(() => {
    getSourceListFn();
  },[])
  return <div>
     <Space
      direction="vertical"
      size="middle"
      style={{
        display: 'flex',
      }}
    >
    <div><Avatar size={30} icon={<UserOutlined />} className='margin-right-10' />王ちゃん</div>
    <Table columns={columns} dataSource={studyItems} pagination={false} />
    </Space>
  </div>
}